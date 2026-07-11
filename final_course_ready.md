# Курс: Архитектура программных систем для IT-команд

**Длительность:** ~10 часов обучения  
**Целевая аудитория:** разработчики, технические лиды, архитекторы

---

## Оглавление

### Часть 1. Архитектурный фундамент
- [0. Базовые принципы разработки](0_Basic_dev_principles.md)
- [4. NFR и CAP теоремы](4_NFR_and_CAP.md)
- [5. DDD и другие подходы](5_DDD_and_so_on.md)

### Часть 2. Проектирование системы
- [1. Монолит или Микросервисы](1_Monolith_vs_Microservices.md)
- [2. Синхронное или Асинхронное взаимодействие](2_Sync_vs_async_in_services.md)
- [3. Многопоточность](3_Multithreading.md)
- [6. Управление общими данными](6_Shared_data_management.md)

### Часть 3. Практика и стоимость
- [7. Расчет метрик и стоимости решения](7_Calculate_solution_metrics_and_costs.md)
- [8. Зачем нужен DevOps и что такое k8s](8_Why_devops_needed_and_what_is_k8s.md)

### Часть 4. Итоговые артефакты
- [9. Артефакты архитектуры](9_Architecture_artifacts.md)

### Дополнительные материалы
- [Сравнение гексагональной и чистой архитектуры](hexagonal_vs_clean.md)

---

## Введение

Цель курса — дать системное понимание ключевых архитектурных решений при разработке распределенных систем. Курс построен как последовательное движение от базовых принципов к практическим задачам оценки стоимости и документирования.

**Как работать с курсом:**
1. Изучайте модули строго по порядку внутри каждой части.
2. Части можно проходить последовательно или выбирать нужные в зависимости от роли.
3. Для закрепления рекомендуется выполнять практические задания (описаны в модулях).

---

## Часть 1. Архитектурный фундамент

### 0. Базовые принципы разработки
**Файл:** [0_Basic_dev_principles.md](0_Basic_dev_principles.md)  
**Ключевые темы:** SOLID, DRY, KISS, YAGNI, композиция против наследования.  
**Цель:** Сформировать общие принципы написания чистого, поддерживаемого кода, на которых строится вся архитектура.

### 4. NFR и CAP теоремы
**Файл:** [4_NFR_and_CAP.md](4_NFR_and_CAP.md)  
**Ключевые темы:** Нефункциональные требования (производительность, надежность, безопасность), теорема CAP и ее следствия для распределенных систем.  
**Цель:** Научиться выявлять и формализовать NFR, понимать компромиссы в распределенных системах.

### 5. DDD и другие подходы
**Файл:** [5_DDD_and_so_on.md](5_DDD_and_so_on.md)  
**Ключевые темы:** Domain-Driven Design, bounded contexts, агрегаты, событийный подход.  
**Цель:** Освоить методы моделирования сложных предметных областей.

---

## Часть 2. Проектирование системы

### 1. Монолит или Микросервисы
**Файл:** [1_Monolith_vs_Microservices.md](1_Monolith_vs_Microservices.md)  
**Ключевые темы:** Сравнение архитектурных стилей, критерии выбора, переход от монолита к микросервисам.  
**Цель:** Научиться выбирать оптимальный стиль для конкретного проекта.

### 2. Синхронное или Асинхронное взаимодействие
**Файл:** [2_Sync_vs_async_in_services.md](2_Sync_vs_async_in_services.md)  
**Ключевые темы:** REST vs gRPC vs очереди сообщений, синхронные и асинхронные паттерны, обработка ошибок.  
**Цель:** Проектировать эффективные коммуникации между сервисами.

### 3. Многопоточность
**Файл:** [3_Multithreading.md](3_Multithreading.md)  
**Ключевые темы:** Параллелизм, конкурентность, потоки, асинхронность, race conditions.  
**Цель:** Обеспечивать производительность и корректность работы внутри сервиса.

### 6. Управление общими данными
**Файл:** [6_Shared_data_management.md](6_Shared_data_management.md)  
**Ключевые темы:** Управление транзакциями, распределенные транзакции, паттерн Saga, консистентность данных.  
**Цель:** Решать проблемы данных в распределенных системах.

---

## Часть 3. Практика и стоимость

### 7. Расчет метрик и стоимости решения
**Файл:** [7_Calculate_solution_metrics_and_costs.md](7_Calculate_solution_metrics_and_costs.md)  
**Ключевые темы:** Оценка производительности, SLA/SLO, расчет стоимости инфраструктуры.  
**Цель:** Обосновывать архитектурные решения с экономической точки зрения.

### 8. Зачем нужен DevOps и что такое k8s
**Файл:** [8_Why_devops_needed_and_what_is_k8s.md](8_Why_devops_needed_and_what_is_k8s.md)  
**Ключевые темы:** Роль DevOps, CI/CD, контейнеризация, Kubernetes.  
**Цель:** Понимать инфраструктурные требования к разрабатываемой системе.

---

## Часть 4. Итоговые артефакты

### 9. Артефакты архитектуры
**Файл:** [9_Architecture_artifacts.md](9_Architecture_artifacts.md)  
**Ключевые темы:** Архитектурные диаграммы, C4 model, Architecture Decision Records (ADR), документация.  
**Цель:** Упаковывать все принятые решения в профессиональные артефакты.

---

## Дополнительные материалы

### Сравнение гексагональной и чистой архитектуры
**Файл:** [hexagonal_vs_clean.md](hexagonal_vs_clean.md)  
Рекомендуется для углубленного изучения после модулей 5 и 9.

---

## Заключение

После прохождения курса вы сможете:
- Анализировать предметную область и выделять ключевые сущности.
- Выбирать архитектурный стиль под конкретную задачу.
- Проектировать взаимодействие между компонентами системы.
- Учитывать нефункциональные требования и экономические ограничения.
- Документировать архитектуру профессиональным способом.

---

## Обратная связь

Вопросы и предложения по курсу оставляйте в [Issues](https://github.com/DAndreev91/course_creator/issues) репозитория.


## Глоссарий

| Термин | Расшифровка | Краткое определение |
|--------|-------------|---------------------|
| ACL | Anticorruption Layer | Слой защиты от "чужой" модели данных |
| ADP | Acyclic Dependencies Principle | Принцип ацикличности зависимостей |
| ADR | Architecture Decision Record | Запись архитектурного решения |
| BDD | Behavior-Driven Development | Разработка через поведение |
| CAP | Consistency, Availability, Partition Tolerance | Теорема распределённых систем |
| CDC | Change Data Capture | Захват изменений данных |
| CQS | Command-Query Separation | Разделение команд и запросов |
| CQRS | Command Query Responsibility Segregation | Разделение моделей чтения и записи |
| DDD | Domain-Driven Design | Предметно-ориентированное проектирование |
| DIP | Dependency Inversion Principle | Принцип инверсии зависимостей |
| DRY | Don't Repeat Yourself | Не повторяйся |
| ISP | Interface Segregation Principle | Принцип разделения интерфейсов |
| KISS | Keep It Simple, Stupid | Будь проще |
| LoD | Law of Demeter | Закон Деметры |
| LSP | Liskov Substitution Principle | Принцип подстановки Лисков |
| NFR | Non-Functional Requirements | Нефункциональные требования |
| OCP | Open-Closed Principle | Принцип открытости/закрытости |
| RPO | Recovery Point Objective | Целевая точка восстановления |
| RTO | Recovery Time Objective | Целевое время восстановления |
| SDP | Stable Dependencies Principle | Принцип стабильности зависимостей |
| SLA | Service Level Agreement | Соглашение об уровне сервиса |
| SLI | Service Level Indicator | Индикатор уровня сервиса |
| SLO | Service Level Objective | Целевой уровень сервиса |
| SoC | Separation of Concerns | Разделение ответственности |
| SRP | Single Responsibility Principle | Принцип единственной ответственности |
| SSOT | Single Source of Truth | Единый источник правды |
| TDD | Test-Driven Development | Разработка через тестирование |
| YAGNI | You Ain't Gonna Need It | Вам это не понадобится |

---

## Рекомендуемая литература

| N | Книга / Статья | Автор | Зачем |
|---|---------------|-------|-------|
| 1 | Clean Architecture | Robert C. Martin | Основы архитектуры: принципы, границы, политики |
| 2 | Building Microservices | Sam Newman | Проектирование, интеграция, эволюция микросервисов |
| 3 | Domain-Driven Design | Eric Evans | DDD: Bounded Context, Ubiquitous Language |
| 4 | Implementing Domain-Driven Design | Vaughn Vernon | Практическое применение DDD |
| 5 | Software Architecture: The Hard Parts | N. Ford, M. Richards, P. Sadalage | Трейдоффы, компромиссы |
| 6 | Documenting Architecture Decisions (ADR) | Michael Nygard | Шаблон ADR, RFC-процесс |
| 7 | Designing Data-Intensive Applications | Martin Kleppmann | CAP, PACELC, распределённые системы |
| 8 | The C4 Model for Visualising Architecture | Simon Brown | C4-диаграммы, Structurizr |

---

## Инструменты для практики

| Инструмент | Назначение | Установка |
|------------|-----------|-----------|
| Structurizr | C4-диаграммы через DSL | brew install structurizr-cli |
| adr-tools | Управление ADR | brew install adr-tools |
| jdeps | Анализ зависимостей Java | Встроен в JDK (jdeps) |
| ArchUnit | Автоматические тесты архитектуры | testImplementation 'com.tngtech.archunit:archunit-junit5:1.0.1' |
| Resilience4j | Circuit Breaker, Retry | io.github.resilience4j:resilience4j-spring-boot3 |
| Mermaid Live | Визуализация диаграмм | https://mermaid.live |
| OpenTelemetry | Распределённый трейсинг | opentelemetry-javaagent.jar |

---

> **Версия курса:** 2.0 (финальная, с учётом рецензий аналитика и разработчика)
>
> **Дата:** 2026
>
> **Лицензия:** Внутреннее использование
